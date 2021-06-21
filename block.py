import pandas as pd

# In this function we are checking if parent transctions exists,
# if it does not exist we use recursion to add the tx_id before the child.
def parentExist(parent, txid, min_weight):
    if str(parent) != "nan":
        set =  str(parent).split(";")
        for i in set:
            if str(txid) in block:

                newindex = input_file[input_file['tx_id']==i].index.item()
                shiftindex = input_file.loc[newindex]

                if min_weight + shiftindex['weight'] <= max_weight:

                    if str(shiftindex) not in block:
                        parentExist(parent, shiftindex)
                        
                        if min_weight + weight <= max_weight:
                            min_weight+=weight
                            block.append(shiftindex)

total_weight, min_weight  = 0,0
max_weight = 4000000
block = []
input_file = pd.read_csv("mempool.csv")
input_file = input_file.sort_values(["fee","weight"],ascending=[False, True]).reset_index(drop=True)
#sorting the mempool by the columns weight and fee to get a block maximisng the fee.

for i in range(len(input_file)):
    txid = input_file.loc[i][0]
    fee = input_file.loc[i][1]
    weight = input_file.loc[i][2]
    parent = input_file.loc[i][3]

    if min_weight + weight <= max_weight:
        if str(txid) not in block:
            parentExist(parent, txid,min_weight)
            if min_weight + weight <= max_weight:
                min_weight+=weight
                block.append(txid)

with open("block.txt","a") as f:
    for line in block:
        f.write(str(line)+ '\n')