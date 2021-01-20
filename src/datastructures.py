
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.family_name = last_name
        self._members = []
        

        # example list of members
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        personExists = False
        for each in self._members:
            if member['first_name'] == each['first_name'] and member['age'] == each['age']:
                personExists = True

        if personExists is not True:
            if member['first_name'] in self._members:
                member['last_name']= self.family_name
                
                if member not in self._members:
                    self._members.append(member)
            else:
                member['last_name']= self.family_name
                member['id'] = self._generateId()
                if member not in self._members:
                    self._members.append(member)
        else: 
            return "Error: User with same Name and Age already exists"

        
            
    def delete_member(self, id):
            for index in range(len(self._members)):
                if self._members[index]['id'] == id:
                    removed = self._members.pop(index)
                    return removed
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
