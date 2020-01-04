Customer-Segmentation
==============================
author: Vincent Sayseng

Audience targeting is essential for a successful ad campaign. Twitter data of users following a [popular premium mobile game account](https://twitter.com/ustwogames?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) were mined. Clustering on the unstructured language data was implemented to determine common interests or keywords that could be exploited in a targeted ad campaign. Insights from this project can be used to create Facebook/Instagram and Twitter ads for Game Revenant's *Where Shadows Slumber*. 

All processing and analysis is contained in the Jupyter notebook, [ios_games_store_analysis.](https://github.com/vin-say/Where-Shadows-Slumber/blob/master/Customer-Segmentation/notebooks/ustwo_twitter_fol_analysis.ipynb)

Scripts used to scrape the online store can be found in another [repository.](https://github.com/vin-say/web-scraping/tree/master/twitter)

Note that the notebook assumes the existence of a data directory (not uploaded to github), with the following layout:

├── data

│   ├── external

│   ├── interim

│   ├── processed

│   └── raw
