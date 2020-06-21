from password_generator import PasswordGenerator

pwd_gen = PasswordGenerator()
pwd_gen.minuchars = 3  # Minimum Number of Upper Cased Letters
pwd_gen.minlchars = 3  # Minimum Number of  Lower Cased Letters
pwd_gen.minnumbers = 3  # Minimum Number of Digits
pwd_gen.minschars = 2 # Minimum Number of Special Characters
pwd_gen.excludeschars = ",$._<>%?*" # Excluded Special Characters

if __name__ == "__main__":
    while True:
        choice = int(input("\n1.Add New / 2.View All / 3.Exit ? "))
        if choice == 1:
            with open("output.txt", "a+") as file:
                pwd_num = input("\nSet Password Length : ")
                place = input("Website/Application : ")
                pwd_gen.maxlen = pwd_gen.minlen = int(pwd_num)
                out = f"{place}:\t{pwd_gen.generate()}\n"
                print(f"+++++++\n{out}+++++++")
                file.write(out)
        elif choice == 2:
            with open("output.txt", "r") as outfile:
                print("\n============================\n")
                for line in outfile:
                    print(line)
                print("============================")
        elif choice == 3:
            print("\n=======.Thank you.=======\n")
            break
        else:
            print("invalid.")
