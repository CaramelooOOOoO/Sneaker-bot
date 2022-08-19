
# BASE Url = https://stockx.com/us/nike-dunk-low-retro-white-black-2021?size=7


a = input("Please type a number 1 if your size has a decimal number like this (.5 for example) if not type 2 #: ") 

if (a == "2"):
    def URLGen(model, size):
        BaseSize = 7
        ShoeSize = size
        RawSize = ShoeSize
        ShoeSizeCode = int(RawSize)
        URL = "https://stockx.com/" + str(model) + "?size=" + str(ShoeSizeCode)
        return URL
    Model = input('Enter the name of the shoe after (https://stockx.com/es-es/) #: ')
    Size = input("Size: ")
    URL = URLGen(Model, Size)
    print(str(URL))
elif (a == "1"):
    def URLGen1(model, size, BehindTheDot):
        BaseSize = 7.5
        ShoeSize = size
        RawSize = ShoeSize
        ShoeSizeCode = int(RawSize)
        BehindTheDot = BehindTheDot
        URL = "https://stockx.com/" + str(model) + "?size=" + str(ShoeSizeCode) + "." + str(BehindTheDot)
        return URL
    Model = input('Enter the name of the shoe after (https://stockx.com/es-es/) #: ')
    Size = input("Size: ")
    BehindTheDot = input("Type here the number behind the dot of your decimal number #:")
    URL = URLGen1(Model, Size, BehindTheDot)
    print(str(URL))



