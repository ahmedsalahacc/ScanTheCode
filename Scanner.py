import re
from State import State
    
class Scanner():
    def __init__(self):
        self.special_chars = {'(':"Open paranthesis", ')': "Closed paranthesis", '+':" Addition Operator", '-': "Subtraction operator",
                             '*': "Multiplication operator", '/':"Division Operator",'=':"Equal (comparison) Operator", 
                             ';': "Semicolon Operator", '<':"Less than operator", '>':"Greater than operator"}
        self.reversed_words = ["if", "then", "else",
                              "end", "repeat", "until", "read", "write"]
        self.white_spaces = ['\n',' ','\t']
        self.table = []
        self.cur_state = None
        
    def scan(self,code):
        self.cur_state= State.START
        stored = ''
        count = 0
        for char in code:
            count+=1
            if self.cur_state == State.START:
                stored = ''
                # scan comments
                if char =='{':
                    self.cur_state = State.INCOMMENT
                    continue
                elif char in self.white_spaces:
                    continue
                elif char.isdigit():
                    self.cur_state = State.INNUM
                    stored+=char
                    continue
                elif char.isalpha():
                    self.cur_state=State.INID
                    stored+=char
                    continue
                elif char == ':':
                    self.cur_state = State.INASSIGN
                elif char in self.special_chars:
                    self.table.append(("special token",char))
                    continue
                    
            elif self.cur_state == State.INNUM:
                if char.isdigit():
                    stored+=char
                    continue
                elif char in self.special_chars:   
                    self.table.append(("Number",stored))
                    self.table.append(("special token",char))
                    self.cur_state = State.START
                    continue
                elif char in self.white_spaces:
                    self.cur_state = State.START
                elif char =='{':
                    self.cur_state = State.INCOMMENT
                else:
                    print('INUM',"ERROR")
                    return f"ERROR {stored+char} {count}"
                
                self.table.append(("Number",stored))
            
            elif self.cur_state == State.INID:
                if char.isalpha():
                    stored+=char
                    continue
                elif char == ':':
                    self.cur_state = State.INASSIGN
                elif char in list(self.special_chars.keys()):               
                    if stored in self.reversed_words:
                        self.table.append(("Reserved", stored))
                    else:
                        self.table.append(("Identifier",stored))
                    self.table.append((self.special_chars[char],char))
                    self.cur_state = State.START
                    continue
                elif char in self.white_spaces:
                    self.cur_state = State.START
                elif char =='{':
                    self.cur_state = State.INCOMMENT
                else:
                    print('INID',"ERROR")
                    return f"ERROR {stored+char} {count}"
                                
                if stored in self.reversed_words:
                    self.table.append(("Reserved", stored))
                else:
                    self.table.append(("Identifier",stored))
                
            elif self.cur_state == State.INCOMMENT:
                if char!='}':
                    continue
                else:
                    self.cur_state = State.START
                    
            elif self.cur_state == State.INASSIGN:
                if char == '=':
                    self.table.append(('Assignment Operator',':='))
                    self.cur_state = State.START
                else:
                    print("ASSIGN","ERROR")
                    return f"ERROR {stored+char} {count}"
            else:
                print("Syntax error")
                return f"ERROR {stored+char} {count}"
        return self.table
                
