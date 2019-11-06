

sample="I LOVE YOU LITTLE"





def lower(samp):
    Caplist=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    lowerlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    newlower=""
    for current_iteration in samp:
        if current_iteration in Caplist:
            new_letter_index=Caplist.index(current_iteration)
            newlower=newlower+lowerlist[new_letter_index]
        else:
            newlower=newlower+current_iteration
    return newlower

print(lower(sample))

