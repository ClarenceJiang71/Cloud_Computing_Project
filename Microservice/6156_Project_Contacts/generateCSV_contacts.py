import pandas as pd

phone_data = {"phoneNo": [4044056253, 1234567890, 3123456789],
              "accountId": [123, 456, 789]
              }
df = pd.DataFrame(phone_data)
df.to_csv("phoneInfo.csv", index=False)

email_data = {"emailAddress": ["yj2737@columbia.edu", "test1@columbia.edu", "test2@columbia.edu"],
              "accountId": [123, 456, 789]
              }
df = pd.DataFrame(email_data)
df.to_csv("emailInfo.csv", index=False)

card_data = {"cardNo": [1234567812345678, 2234567822345678, 3234567842345678],
             "accountId": [123, 456, 789],
             "cvc": [111, 222, 333],
             "expirationDate": ["10/25", "11/25", "12/25"],
             "holderFirst": ["Clarence", "Brian", "Donald"],
             "holderLast": ["Jiang", "Hello", "Ferguson"],
             "cardType": ["D", "C", "C"],
             "billingAddressId": [1, 2, 3]
             }
df = pd.DataFrame(card_data)
df.to_csv("cardInfo.csv", index=False)

address_data = {"id": [1, 2, 3],
                "accountId": [123, 456, 789],
                "street": ["400 W 113 St", "50 W 109 St", "1080 Amsterdam Avenue"],
                "aptNo": [119, 234, 431],
                "city": ["New York", "New York", "New York"],
                "state": ["NY", "NY", "NY"],
                "zip": [10025, 10024, 10026]
                }
df = pd.DataFrame(address_data)
df.to_csv("addressInfo.csv", index=False)

# ds1 = pd.read_csv("phoneInfo.csv")
# ds2 = pd.read_csv("emailInfo.csv")
# ds3 = pd.read_csv("cardInfo.csv")
# ds4 = pd.read_csv("addressInfo.csv")
# print("space") # save a line to create breakpoint

