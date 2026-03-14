def get_average(numbers) : 
    if not numbers : 
        return 0
    return sum(numbers)/len(numbers)
def is_even(number) : 
    return number%2==0

if __name__ == "__main__" : 
    sample_nums=[10,20,30]
    print(f"[테스트] {get_average(sample_nums)}")
    print(f"[테스트] {is_even(sample_nums[1])}")