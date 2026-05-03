# !pip install pandas plotly faker

import pandas as pd
import random
import plotly.express as px
from faker import Faker


# step 1
fake = Faker()

sentiments = ['Positive', 'Negative', 'Neutral']
hashtags = ['#AI', '#Tech', '#DataScience', '#Python', '#Startup']

data = []

for i in range(200) :
  post = {
      'user': fake.user_name(),
      'post_text': fake.sentence(),
      'sentiment': random.choice(sentiments),
      'likes': random.randint(10,500),
      'comments': random.randint(1,100),
      'shares': random.randint(1,50),
      'hashtag': random.choice(hashtags)
  }
  data.append(post)

df = pd.DataFrame(data)
df.head()


# step 2
df['engagement'] = df['likes'] + df['comments'] + df['shares']

df.head()

#step 3
sentiment_count = df['sentiment'].value_counts().reset_index()
sentiment_count.columns = ['Sentiment', 'Count']

fig = px.pie(
    sentiment_count,
    values='Count',
    names='Sentiment',
    title="Sentiment Distribution"
)

fig.show()

#step 4
hashtag_count = df['hashtag'].value_counts().reset_index()
hashtag_count.columns = ["Hashtag", "Count"]

fig = px.bar(
    hashtag_count,
    x= "Hashtag",
    y="Count",
    title="Trending Hashtags"
)

fig.show()

#step 5
fig = px.scatter(
    df,
    x="likes",
    y="shares",
    color="sentiment",
    size='engagement',
    title="Engagement Analysis"
)

fig.show()

#step 6
top_posts = df.sort_values(by="engagement", ascending=False).head(10)

top_posts[["user", "post_text", "engagement"]]

#step 7
report = {
    "Total Posts": len(df),
    "Average Likes": df["likes"].mean(),
    "Average comments": df['comments'].mean(),
    "Average  Shares": df['shares'].mean(),
    "Most Trending Hashtag": df['hashtag'].mode()[0]
}

report