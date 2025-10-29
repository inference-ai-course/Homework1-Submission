# Reddit Investment Intelligence System - User Guide

## 🎯 Overview

This system automatically scrapes r/CanadianInvestor, analyzes stock mentions, and generates investment reports using Claude Desktop with MCP plugins.

## 📋 Prerequisites

### Required MCP Plugins:
1. **Puppeteer MCP** - Browser automation and web scraping
2. **Filesystem MCP** - File reading/writing operations  
3. **Notion MCP** - Notion workspace integration

### Configuration Requirements:
- Claude Desktop properly configured with MCP plugins
- Filesystem MCP access to your Desktop folder
- Notion MCP connected to your Notion workspace

## 🚀 Quick Start Guide

### Option 1: Full Automated Run

Simply say to Claude:
```
"Run the Reddit investment scraping workflow for r/CanadianInvestor. 
Scrape posts, analyze stock mentions, save to CSV, create Notion database, 
and generate analysis reports."
```

### Option 2: Step-by-Step Execution

**Step 1: Web Scraping**
```
"Navigate to reddit.com/r/CanadianInvestor and scrape the top 50 posts. 
Extract titles, authors, upvotes, comments, and timestamps."
```

**Step 2: Data Analysis**
```
"Analyze the scraped Reddit data for stock ticker mentions, sentiment, 
and investment relevance. Categorize by context type."
```

**Step 3: File Export**
```
"Save the analyzed data to a CSV file named scraped_data_YYYY_MM_DD.csv 
on my Desktop. Include all relevant columns."
```

**Step 4: Notion Database**
```
"Create a Notion database called 'Investing' with fields for stock ticker, 
date, company name, analysis summary, investment potential, risk level, 
sentiment, upvotes, and comments. Then populate it with the top 5 opportunities."
```

**Step 5: Report Generation**
```
"Generate a comprehensive investment analysis report and save it as both 
a local Markdown file and add it to my Notion workspace."
```

## 📁 Output Files

After execution, you'll find these files on your Desktop:

1. **scraped_data_[DATE].csv**
   - Raw scraped data in CSV format
   - Columns: Date, Stock_Ticker, Company_Name, Post_Title, Author, Upvotes, Comments_Count, Investment_Context, Sentiment

2. **investment_analysis_report_[DATE].md**
   - Comprehensive analysis report
   - Includes: Executive summary, key findings, top opportunities, risk factors, recommendations

3. **EXECUTION_SUMMARY.md**
   - Detailed execution log
   - Processing statistics
   - Success metrics

## 🔧 Customization Options

### Change Target Subreddit:
```
"Scrape r/stocks instead of r/CanadianInvestor"
```

### Adjust Number of Posts:
```
"Scrape 100 posts instead of 50"
```

### Focus on Specific Sector:
```
"Only analyze posts about technology stocks"
```

### Custom Date Range:
```
"Scrape posts from the last 7 days only"
```

### Different Output Location:
```
"Save files to Documents folder instead of Desktop"
```

## 📊 Understanding the Output

### Investment Relevance Levels:
- **High**: Direct stock mentions, ETF discussions, earnings reports
- **Medium**: Economic policy discussions affecting markets
- **Low**: General discussion, personal finance questions

### Sentiment Classification:
- **Positive**: Bullish indicators, growth opportunities, positive news
- **Negative**: Bearish signals, job cuts, declining metrics
- **Neutral**: Informational, balanced discussion

### Risk Levels:
- **Low**: Large-cap stocks, diversified ETFs, stable companies
- **Medium**: Mid-cap stocks, sector-specific funds, moderate volatility
- **High**: Small-cap stocks, single stock concentration, operational issues

## 🔍 Notion Database Structure

### Database Name: "Investing"

### Fields:
1. **Stock_Ticker** (Title) - Primary identifier
2. **Date** (Date) - Analysis date
3. **Company_Name** (Rich Text) - Full company names
4. **Source_Post** (URL) - Link to original Reddit post
5. **Analysis_Summary** (Rich Text) - Key insights
6. **Investment_Potential** (Select) - High/Medium/Low
7. **Risk_Level** (Select) - Low/Medium/High  
8. **Sentiment** (Select) - Positive/Neutral/Negative
9. **Upvotes** (Number) - Community engagement metric
10. **Comments** (Number) - Discussion volume
11. **Notes** (Rich Text) - Additional observations

## 📈 Using the Analysis

### For Buy Decisions:
Look for:
- HIGH Investment Potential
- LOW to MEDIUM Risk Level  
- POSITIVE Sentiment
- High upvotes/comments (strong community validation)

### For Sell/Avoid Decisions:
Watch for:
- LOW Investment Potential
- HIGH Risk Level
- NEGATIVE Sentiment
- Job cuts, restructuring news

### For Watch List:
Consider:
- MEDIUM Investment Potential
- Near-term catalysts (earnings, IPOs)
- HIGH Risk Level but positive trends

## 🔄 Automated Scheduling

### Daily Scraping (Manual):
Run the command each morning:
```
"Run daily Reddit investment scan for r/CanadianInvestor"
```

### Weekly Summary (Manual):
Run every Sunday:
```
"Run weekly Reddit investment analysis and compare to last week's data"
```

### Monthly Review (Manual):
Run on the 1st of each month:
```
"Generate monthly investment intelligence report from Reddit data 
and identify trends over the past 30 days"
```

## ⚠️ Important Limitations

### Data Quality:
- Reddit sentiment represents retail investors only
- Not professional investment advice
- Bias toward popular/meme stocks possible
- Sentiment can be manipulated

### Technical Constraints:
- Reddit may rate-limit excessive scraping
- Post structure changes may break parser
- Ticker detection is pattern-based (not 100% accurate)
- Comments not analyzed (titles only)

### Legal/Ethical:
- Respect Reddit's Terms of Service
- Don't over-scrape (recommended: max once per day)
- Data is for personal use only
- Not financial advice - do your own research

## 🐛 Troubleshooting

### "Failed to navigate to URL"
- Check internet connection
- Reddit may be down
- Try again in a few minutes

### "No posts found"
- Subreddit structure may have changed
- Adjust CSS selectors if needed
- Try different subreddit

### "Filesystem error"
- Check Desktop folder permissions
- Ensure Filesystem MCP has proper access
- Try different save location

### "Notion database creation failed"
- Verify Notion MCP connection
- Check Notion workspace permissions
- Try creating database manually first

### "No stock tickers detected"
- Posts may not mention specific stocks
- Adjust ticker detection regex
- Check for new ticker formats

## 💡 Pro Tips

1. **Run during market hours** for most relevant discussions
2. **Compare week-over-week** to identify trending stocks
3. **Cross-reference with other sources** before trading
4. **Focus on high-engagement posts** (100+ upvotes)
5. **Read the original posts** for full context
6. **Watch for catalyst dates** (earnings, IPOs, policy changes)
7. **Track recommendation performance** to validate accuracy
8. **Build historical database** for trend analysis
9. **Combine with fundamental analysis** before investing
10. **Use as idea generation** not sole decision-making tool

## 🔐 Security & Privacy

- All data stored locally on your machine
- Notion data visible only to you (unless shared)
- No external APIs called (except Reddit, Notion)
- No personal data collected
- No trading executed automatically
- Always review before making investment decisions

## 📚 Additional Resources

### Reddit Investment Subreddits:
- r/CanadianInvestor - Canadian stocks & investing
- r/stocks - General stock discussion
- r/investing - Long-term investment strategies
- r/wallstreetbets - High-risk trading (use with caution)
- r/dividends - Dividend investing focus

### Recommended Reading:
- Notion database for tracking mentioned stocks over time
- CSV analysis in Excel/Google Sheets for trends
- Markdown reports for quick reference

### Further Automation Ideas:
- Email alerts for high-confidence opportunities
- Price tracking integration via API
- Portfolio rebalancing suggestions
- Sentiment dashboard visualization
- Multi-subreddit aggregation

## 📞 Support

For issues with:
- **Claude Desktop**: Check Claude.ai support
- **MCP Plugins**: Review MCP documentation  
- **This Workflow**: Refer to EXECUTION_SUMMARY.md for details

## 📄 License & Disclaimer

**License**: For personal use only

**Disclaimer**: This system is for informational purposes only. The output does not constitute financial advice. Always conduct your own research and consult with a qualified financial advisor before making investment decisions. Past performance does not guarantee future results. Investing carries risk of loss.

---

**Version**: 1.0  
**Last Updated**: October 28, 2025  
**Created by**: Automated Investment Intelligence System  
**Powered by**: Claude Desktop + MCP