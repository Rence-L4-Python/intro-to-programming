# USB Shopper

## A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
## Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
## You will need to use the arithmetic operators to complete this exercise.


USB=6
MaxAllowance=50

TotalSticks=(MaxAllowance//USB)
CashPaid=(TotalSticks*USB)
Result=(MaxAllowance-CashPaid)

## printing with f-string to avoid spacing between '£' and the cash remainder
print("You can buy:", TotalSticks, "USB Sticks" "\n", f"Your remaining cash is: £{Result}")
