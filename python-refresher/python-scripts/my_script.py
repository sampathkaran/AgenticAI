x = 100
print(x)

def my_function():
    print("this my function")

# here whatteve we define under main it will be not excuted during import
# it will run only when we executre this file standalone
if __name__ == "__main__":
 my_function()