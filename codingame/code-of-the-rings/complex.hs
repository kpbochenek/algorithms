import System.IO
import Control.Monad
import Data.Char
import Data.List


moveLeft = '<'
moveRight = '>'
increase = '+'
decrease = '-'
spell = '.'
startLoop = '['
stopLoop = ']'


a0 = ord 'A' - 1
z0 = ord 'Z' + 1
alphabetLen = z0 - a0
zonesLen = 30

letter_distance_move :: Char -> Char -> (Int, Char)
letter_distance_move l1 l2
  | l1 == l2 = (0, increase)
  | l1 == ' ' = min (l2o - a0, increase) (z0 - l2o, decrease)
  | l2 == ' ' = min (z0 - l1o, increase) (l1o - a0, decrease)
  | l1o < l2o = min (l2o - l1o, increase) (alphabetLen - l2o + l1o, decrease)
  | otherwise = min (l1o - l2o, decrease) (alphabetLen - l1o + l2o, increase)
  where
    l1o = ord l1
    l2o = ord l2


replaceAtIndex n item ls = a ++ (item:b) where (a, (_:b)) = splitAt n ls


zone_distance_move :: Int -> Int -> (Int, Char)
zone_distance_move z1 z2
  | z1 == z2 = (0, moveRight)
  | z1 < z2 = min (z2 - z1, moveRight) (zonesLen - z2 + z1, moveLeft)
  | otherwise = min (z1 - z2, moveLeft) (zonesLen - z1 + z2, moveRight)


-- zones  pos  output
data GameState = GameState [Char] Int [Char]
instance Eq GameState where
  (GameState z1 p1 o1) == (GameState z2 p2 o2) = (z1, p1, o1) == (z2, p2, o2)
instance Ord GameState where
  (GameState z1 p1 o1) `compare` (GameState z2 p2 o2) = (length o1) `compare` (length o2)

get_output (GameState zones pos output) = output


make_move :: GameState -> Int -> Char -> GameState
make_move (GameState zones pos output) newZone newLetter = 
  GameState nZones newZone (output ++ (replicate moveZoneNum moveZoneHow) ++ (replicate moveLetterNum moveLetterHow) ++ [spell])
  where
    (moveZoneNum, moveZoneHow) = zone_distance_move pos newZone
    (moveLetterNum, moveLetterHow) = letter_distance_move (zones !! pos) newLetter
    nZones = replaceAtIndex newZone newLetter zones

splits = 1
deep = 3

generate :: GameState -> [Char] -> [GameState]
generate gs [] = [gs]
generate gs words =
  intercalate [] [generate newgs (tail words)| newgs <- take splits (sort moves)]
  where
    moves = [make_move gs i (head words) | i <- [0..zonesLen-1]]


go :: [GameState] -> String -> [GameState]
go gs [] = gs
go gs magicPhrase =
  go (take 10 (sort states)) right
  where
    states = intercalate [] [generate state left | state <- gs]
    (left, right) = splitAt deep magicPhrase

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    magicphrase <- getLine

    let states = [(GameState (replicate 30 ' ') 0 [])]
    putStrLn (get_output $ head $ go states magicphrase)
