def GGGGotate(lol):
    print(f"[2] from GGGGotate: {lol}")
    bit = lol << 1
    print(f"[4] from GGGGotate: {lol} bit: {bit}")
    movebit = bit & 255
    print(f"[7] movebit from lol --->: {movebit}")
    if (lol > 127 ):
        movebit = movebit | 1
        print(f"[10] movebit from lol --->:{movebit}")
    return (movebit)
def main():
    value = input("Enter your value: ")
    print(f"[14] value -->  {value}")
    ListMoveBit = []
    print(f"[16] ListMoveBit:{ListMoveBit}")
    Index_Move_bit = 1
    print(f"[18] Index_Move_bit: {Index_Move_bit}")
    Index_Value = 0
    print(f"[20] Index_Value: {Index_Value}")
    ORD_value = []
    print(f"[22] ORD_value: {ORD_value}")
    ORD_key = []
    print(f"[24] ORD_key: {ORD_key}")
    Under_10 = []
    print(f"[26] Under_10: {Under_10}")
    Index_star = 0
    print(f"[28] Index_star: {Index_star}")
    Final_encrypted = ""
    print(f"[30] Final_encrypted: {Final_encrypted}")
    Passs = []
    print(f"[32] Passs: {Passs}")
    List_values_back = []
    print(f"[34] List_values_back: {List_values_back}")
    Uncrypt = []
    print(f"[36] Uncrypt: {Uncrypt}")
    for i in value:
        ORD_value.append(ord(i))
        print(f"[39] ORD_value: {ORD_value} , i: {ord(i)} value: {value}")

    print(f"[40] *2* -->>i: {i} value: {value}")
    a = ord("a")
    print(f"[42] a = ord('a') = {a}")
    ORD_key.append(a)

    print(f"[45] ORD_key:->{ORD_key} ORD_value:->{ORD_value}")
    lol = int(ORD_key[0]) ^ int(ORD_value[0])
    ListMoveBit.append(GGGGotate(lol))
    print(f"[49] KEY:{ORD_key[0]} ^ VAL:{ORD_value[0]} = lol: {lol}")
    print(f"[50] List_values_back : {List_values_back}, ListMoveBit: {ListMoveBit}  lol: {lol}")
    for chars in ORD_value:
        print(f"[52] {chars} ORD_VALUE {ORD_value}")
        if Index_Value == 0:
            print(f"[54] > index_value {Index_Value}")
            Index_Value += 1
            print(f"[55] lol if ----->>>> {lol}")
            pass
        else:
            print(f"[58] lol else:--->>> {lol}")
            lol = int(ListMoveBit[Index_Value-1]) ^ int(chars)
            ListMoveBit.append(GGGGotate(lol))
            Index_Value += 1
            print(f"[63] ListMoveBit: {ListMoveBit} ,\n {int(ListMoveBit[Index_Value-1])},  chars: {chars}  Index_Value: {Index_Value-1}, lol : {lol}")
    print(f"[64] chars: {chars}  , lol : {lol}")
    for i in ListMoveBit:
        Under_10.append("0")
        print(f"[66]{i} ,  ListMoveBit: {ListMoveBit}, | {Under_10}")
    print(f"[67] for i: {i} in  ListMoveBit: {ListMoveBit}")

    for i in ListMoveBit:
        print(f"[70] {i} {ListMoveBit}")
        if (i < 9):
            Under_10[Index_star] = "1"
        Index_star += 1
    print(f"[73] ListMoveBit: {ListMoveBit}")

    for i in ListMoveBit:
        x = hex(i)
        print(f"[78] x = hex(i): {x}, i=: {i}")
        val = x[2:]
        print(f"[80] val: {val}")
        if(i > 9) and (i < 16):
            Final_encrypted = Final_encrypted + "0" + val
            print(f"[83] IF: Final_encrypted {Final_encrypted}")
        else:
            if (i<10):
                Final_encrypted = Final_encrypted + "0" + val
                print(f"[87] IF: Final_encrypted {Final_encrypted}, i: {i}")

            else:
                Final_encrypted = Final_encrypted + val
                print(f"[91] IF: Final_encrypted {Final_encrypted} , i: {i}")

        print(f"[89] i: {i}")
    print(f"[88] i: {i} ListMoveBit: {ListMoveBit}")

    print("\nThe encrypted message is:")
    print(Final_encrypted + "\n")
if __name__ == '__main__':
    main()