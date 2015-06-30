import System.IO
import Control.Monad

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE

    input_line <- getLine
    let input = words input_line
    let lx = read (input!!0) :: Int -- the X position of the light of power
    let ly = read (input!!1) :: Int -- the Y position of the light of power
    let tx = read (input!!2) :: Int -- Thor's starting X position
    let ty = read (input!!3) :: Int -- Thor's starting Y position
    loop lx ly tx ty

loop :: Int -> Int -> Int -> Int -> IO ()
loop lx ly tx ty = do
    input_line <- getLine
    let e = read input_line :: Int -- The level of Thor's remaining energy, representing the number of moves he can still make.

    let (nlx, xs) = if lx < tx then (lx + 1, "W")
        else if lx > tx then (lx - 1, "E")
        else (lx, "")
    let (nly, ys) = if ly < ty then (ly + 1, "N")
        else if ly > ty then (ly - 1, "S")
        else (ly, "")

    putStrLn (ys ++ xs)

    loop nlx nly tx ty
