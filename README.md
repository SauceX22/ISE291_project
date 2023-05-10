Its clear from the summary above that the coulms (RERA, BHK_OR_RK, SQUARE_FT, READY_TO_MOVE) has some NaN values and need to be fixed. We will replace catagorical data with the mode of the coulmns and the numrical data with the mean of the coulmn.

---

|         name         |    type    |                 description                 |
| :-------------------: | :---------: | :------------------------------------------: |
|       POSTED_BY       | Categorical | Category marking who has listed the property |
|  UNDER_CONSTRUCTION  |   Nominal   |          Under Construction or Not          |
|         RERA         |   Nominal   |             Rera approved or Not             |
|        BHK_NO.        |  Numerical  |               Number of Rooms               |
|       BHK_OR_RK       | Categorical |               Type of property               |
|       SQUARE_FT       |  Numerical  |    Total area of the house in square feet    |
|     READY_TO_MOVE     |   Nominal   |    Category marking Ready to move or Not    |
|        RESALE        |   Nominal   |        Category marking Resale or not        |
|        ADDRESS        | Categorical |           Address of the property           |
|       LONGITUDE       |  Numerical  |          Longitude of the property          |
|       LATITUDE       |  Numerical  |           Latitude of the property           |
| TARGET(PRICE_IN_LACS) |  Numerical  |              The property price              |

# header
