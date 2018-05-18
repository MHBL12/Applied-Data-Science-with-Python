
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[12]:

import matplotlib.pyplot as plt  
import pandas as pd
#import plotly.plotly as py  
#import plotly.tools as tls

# Read the data into a pandas DataFrame.    
gender_degree_data = pd.read_csv("http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv")    
      
# the number of lines being plotted on it.    
# Common sizes: (10, 7.5) and (12, 9)    
plt.figure(figsize=(12, 14))    
  
# Remove the plot frame lines. They are unnecessary chartjunk.    
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    
  
# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    
  
# Limit the range of the plot to only where the data is.    
# Avoid unnecessary whitespace.    
plt.ylim(0, 90)    
plt.xlim(1968, 2014)    
  
# Make sure axis ticks are large enough to be easily read.        
plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)    
plt.xticks(fontsize=14)    
  
# Provide tick lines across the plot to help trace along    
# the axis ticks. Make sure that the lines are light and small so they    
# don't obscure the primary data lines.    
for y in range(10, 91, 10):    
    plt.plot(range(1968, 2012), [y] * len(range(1968, 2012)), "--", lw=0.5, color="black", alpha=0.3)    
  
# Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")    
   
# plotted the majors in order of the highest % in the final year.    
majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',    
          'Foreign Languages', 'English', 'Communications\nand Journalism',    
          'Art and Performance', 'Biology', 'Agriculture',    
          'Social Sciences and History', 'Business', 'Math and Statistics',    
          'Architecture', 'Physical Sciences', 'Computer Science',    
          'Engineering']    
  
for rank, column in enumerate(majors):      
    plt.plot(gender_degree_data.Year.values,    
            gender_degree_data[column.replace("\n", " ")].values,    
            lw=2.5)    
  
    # Add a text label to the right end of every line.   
    # adding specific offsets y position because some labels overlapped.    
    y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5    
    if column == "Foreign Languages":    
        y_pos += 0.5    
    elif column == "English":    
        y_pos -= 0.5    
    elif column == "Communications\nand Journalism":    
        y_pos += 0.75    
    elif column == "Art and Performance":    
        y_pos -= 0.25    
    elif column == "Agriculture":    
        y_pos += 1.25    
    elif column == "Social Sciences and History":    
        y_pos += 0.25    
    elif column == "Business":    
        y_pos -= 0.75    
    elif column == "Math and Statistics":    
        y_pos += 0.75    
    elif column == "Architecture":    
        y_pos -= 0.75    
    elif column == "Computer Science":    
        y_pos += 0.75    
    elif column == "Engineering":    
        y_pos -= 0.25    
  
    # make sure that all labels are large enough to be easily read        
    plt.text(2011.5, y_pos, column, fontsize=14)    
  
# matplotlib's title() call centers the title on the plot, but not the graph,      
plt.text(1995, 93, "Percentage of Bachelor's degrees conferred to women in the U.S.A."    
       ", by major (1970-2011)", fontsize=17, ha="center")      
plt.text(1966, -8, "Data source: https://nces.ed.gov/programs/digest/current_tables.asp"    
       , fontsize=10)    
    
#plt.savefig("percent-bachelors-degrees-women-usa.png", bbox_inches="tight")  
plt.show()
# Grab figure object and link it to variable (must be in same cell as figure)
#dataviz1 = gcf()
#onvert a matplotlib figure object dataviz1 into a Plotly figure
#py.iplot_mpl(dataviz1, resize=False, filename='dataviz1', width=960, height=1120)


# In[ ]:




# In[ ]:





# In[ ]:



