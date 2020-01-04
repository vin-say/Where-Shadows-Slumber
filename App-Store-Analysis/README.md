App-Store-Analysis
==============================
author: Vincent Sayseng

Every mobile game available on iOS has an [online profile](https://apps.apple.com/us/app/where-shadows-slumber/id1221749074) listing features of the app, such as price, age rating, and review score distribution. These features were scraped and prepared to fit a regression model that aims to predict the popularity of a given game. Knowing the most important features that are correlated with game popularity will inform the business strategy of Game Revenant. 

All processing and analysis is contained in the Jupyter notebook, [ios_games_store_analysis.] (https://github.com/vin-say/Where-Shadows-Slumber/blob/master/App-Store-Analysis/notebooks/ios_games_store_analysis.ipynb) 

Scripts used to scrape the online store can be found in another [repository.](https://github.com/vin-say/web-scraping/tree/master/iosgames)

Note that the notebook assumes the existence of a data directory (not uploaded to github), with the following layout:
├── data
│   ├── external      
│   ├── interim    
│   ├── processed     
│   └── raw            


