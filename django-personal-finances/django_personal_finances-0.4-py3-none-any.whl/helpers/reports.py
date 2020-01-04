from finances.models import BudgetCategories


class ReportQueryResults:
    def __init__(self, amount_dict, query_type):
        """
        Params
        ------
        amount_dict: BudgetCategories
            finances.models
        query_type: str
            Must be either "Annual" or "Monthly"
        """
        self.category_obj = BudgetCategories.objects.get(pk=amount_dict["category"])
        self.category = self.category_obj.category
        
        # Convert the budget categories into units
        if query_type == self.category_obj.category_type:
            self.category_budget = self.category_obj.amount
        if query_type == "Monthly" and self.category_obj.category_type == "Annual":
            self.category_budget = self.category_obj.amount / 12
        if query_type == "Annual" and self.category_obj.category_type == "Monthly":
            self.category_budget = self.category_obj.amount * 12
        
        self.total_amount = amount_dict["total_amount"]
        self.budget_percent = (self.total_amount / self.category_budget * 100) if self.category_budget != 0 else 0
        self.exceeded_percent = 0 if (self.budget_percent < 0) else (self.budget_percent - 100)
        self.isExceeded = (self.budget_percent > 100)
