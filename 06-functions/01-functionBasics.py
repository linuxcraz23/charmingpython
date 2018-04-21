"""
function
    -- block of code that performs a single task
    -- makes the code reusable, modular
    -- types
        -- built-in
        -- user defined
    -- always define before calling
    -- can have parameters
    -- do not define return type. why?
    -- can have multiple returns
"""

# a function returning a value
def countStars(starString):
    stCount = 0
    for ch in starString:
        if ch == '*':
            stCount +=1
    return stCount

# parameterized function
def logNstars(count):
    print ('*'*count)

# another function
def logStars():
    print ('*'*50)

# function definition
def main():
    print ("this is main function")
    logStars()

    count = input("enter count of stars : ")
    logNstars(int(count))

    starString = "* there * are * 5 * stars*****"
    print ("count of stars : %d " % countStars(starString))

# this is actually the first line to be executed
# function call
main()
