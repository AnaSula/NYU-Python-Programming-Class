#Indentation Problems

foo = long_function_name(var_one, var_two,
    var_three, var_four)

#should be: Aligned with opening delimiter.

foo = long_function_name(var_one, var_two,
                        var_three, var_four)

def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

#should be: More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

#Operations Problems
# operators: prefix or postfix?
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

#should be: prefix because it's better for readability

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

#Blank Line Problems

def top_level_func():
    print("important processing going on here")

def second_func():


    print("another gravely important function")

#should be

def top_level_func():
    print("important processing going on here")


def second_func():
    print("another gravely important function")

#Naming Problems

def topLevelFunc():
    print("important processing going on here")
    mixedCaseVariables = True

#should be

def TopLevelFunc():
    print("important processing going on here")
    MixedCaseVariables = True
