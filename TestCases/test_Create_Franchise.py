import requests

from Methods.Create_Franchise import CreateFranchise


class Create_Franchise(CreateFranchise):
    def test_create_franchise_with_valid_credentials(self):
        flag = self.Create_Franchise_with_valid_credentials()
        assert flag is True
