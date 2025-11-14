cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai",]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print(len(list))

    def print_list(list):
        for item in list:
            print(item, end=" ")


            print_list(cities)
            print()

