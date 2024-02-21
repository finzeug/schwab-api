import json
from datetime import datetime

def generate_option_symbol(Root, expiration_date, Strike_Price, Type):
    """
        expiration_date (datetime) - the expiration date you selected, 
        Strike_Price (float) - strike price of the option you picked,
        Type (str) - Must be "Call" or "Put"
        
        Returns the option symbol (str).
    """
    Strike_Price = int(Strike_Price*10000)
    Strike_Price = str(Strike_Price)
    #calculate number of leading zeroes requires to make 10 digit string
    N=10-len(Strike_Price)
    #add leading zeroes to make it 10 digits
    Strike_Price = '0'*N+Strike_Price
    if Type == "Call" or Type == "Put"
        Type = "C" if Type == "Call" else "P"
    else:
        raise ValueError("Type is invalid, it must be 'Call' or 'Put'")
    expiration_date = expiration_date.strftime("%m%d%y")
    return Root+"  "+Expiration_YYMMDD+Type+Strike_Price

class OptionSeries:
    def __init__(self, option_series):
        """
            Option series class used to process data from the json response
        """
        self.option_series = option_series

    def get_expiration_dates(self):
        """
            Returns the expiration dates in datetime format.
        """
        dates = []
        for i in self.option_series["Expirations"]:
            dates.append(datetime.strptime(i["Date"],"%m/%d/%Y"))
        return dates

    def get_strikes(self, expiration_date):
        """
            expiration_date (datetime) - date at which option expires 
            Returns a list of strike prices matching the date
        """
        sub_strikes = []
        strikes = []
        for i in self.option_series["Expirations"]:
            if i["Date"] == expiration_date.strftime("%m/%d/%Y"):
                Roots = i["Roots"]
                for r in Roots:
                    for s in i["Strikes"]:
                        if r in s["Root"]:
                            sub_strikes.append(s["Price"])
                    strikes.append(sub_strikes)        
        return strikes

    def get_roots(self, expiration_date):
        """
            expiration_date (datetime)
        """
        Roots = self.option_series["Roots"]
        #roots stores the indexes of Roots
        roots = []
        for i in self.option_series["Expirations"]:
            if i["Date"] == expiration_date.strftime("%m/%d/%Y"):
                roots = i["Roots"]
        return [Roots[r] for r in roots]

