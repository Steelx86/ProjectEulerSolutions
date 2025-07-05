#!/usr/bin/env python3

# Way too much code for this problem


def moves_gen(height=20, length=20, gen_number) -> list[str]:
    moves = []
    
    
    
    for i in range(height):
        for j in range(length):
            moves.append("right")
        
        moves.append("down")
        
    return moves


def grid_runner(move_list):
    pass


if __name__ == "__main__":
    pass
