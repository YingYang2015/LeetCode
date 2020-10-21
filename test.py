x = [['John','john00@mail.com','john_newyork@mail.com','johnsmith@mail.com'],
    ['Mary','mary@mail.com'],
    ['John','johnnybravo@mail.com']]
import collections

dict = collections.defaultdict(list)

dict = {'Name': 'Zabra', 'Age': 7}
print("Value : %s" %  dict.get('Age'))
print("Value : %s" %  dict.get('Education'))

for i in dict.items():
    print(i)