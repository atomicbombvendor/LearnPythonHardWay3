import os

root = "D:\QA\GEDF\GeDataFeed-MOCAL4936\GEDF\\"
folder = [
    "@Region@\CompanyProfile\GeneralProfile\Monthly",
    "@Region@\CompanyProfile\GeneralProfileCombined\Monthly",
    "@Region@\CompanyProfile\IndexDJ\Monthly",
    "@Region@\CompanyProfile\IndexSNP\Monthly",
    "@Region@\CompanyProfile\LongDescription\Monthly",
    "@Region@\CompanyProfile\MediumDescription\Monthly",
    "@Region@\CorporateAction\CapitalRepayment\Monthly",
    "@Region@\CorporateAction\CashDividend\Monthly",
    "@Region@\CorporateAction\MergerAndAcquisition\Monthly",
    "@Region@\CorporateAction\RightsIssue\Monthly",
    "@Region@\CorporateAction\SpinOff\Monthly",
    "@Region@\CorporateAction\StockSplit\Monthly",
    "@Region@\CorporateCommunication\CorporateCalendar\Monthly",
    "@Region@\CUSIPandISIN\CUSIPandISIN\Monthly",
    "@Region@\ExecutiveInsight\BoardCompensationCurrent\Monthly",
    "@Region@\ExecutiveInsight\BoardCompensationHistory\Monthly",
    "@Region@\ExecutiveInsight\ExecutiveCompensationCurrent\Monthly",
    "@Region@\ExecutiveInsight\ExecutiveCompensationHistory\Monthly",
    "@Region@\ExecutiveInsight\MembershipCurrent\Monthly",
    "@Region@\ExecutiveInsight\MembershipHistory\Monthly",
    "@Region@\ExecutiveInsight\OfficerDirectorCurrent\Monthly",
    "@Region@\ExecutiveInsight\OfficerDirectorHistory\Monthly",
    "@Region@\ExecutiveInsight\OptionsExeCurrent\Monthly",
    "@Region@\ExecutiveInsight\OptionsExeHistory\Monthly",
    "@Region@\ExecutiveInsight\OutstandingAwardsCurrent\Monthly",
    "@Region@\ExecutiveInsight\OutstandingAwardsHistory\Monthly",
    "@Region@\ExecutiveInsight\SayOnPayCurrent\Monthly",
    "@Region@\ExecutiveInsight\SayOnPayHistory\Monthly",
    "@Region@\ExecutiveInsight\StockOptionGrantCurrent\Monthly",
    "@Region@\ExecutiveInsight\StockOptionGrantHistory\Monthly",
    "@Region@\ExecutiveInsight\VotingReportCurrent\Monthly",
    "@Region@\ExecutiveInsight\VotingReportHistory\Monthly",
    "@Region@\Fundamental\EarningRatios\Monthly",
    "@Region@\Fundamental\EarningReports\Monthly",
    "@Region@\Fundamental\FinancialStatements\Monthly",
    "@Region@\Fundamental\OperationRatios\Monthly",
    "@Region@\Fundamental\PriceMultipleRatios\Monthly",
    "@Region@\Fundamental\Segmentation\Monthly",
    "@Region@\Fundamental\ValuationRatios\Monthly",
    "@Region@\GlobalCorporationAction\MergerAndAcquisition\Monthly",
    "@Region@\GlobalCorporationAction\ShareCorporateActions\Monthly",
    "@Region@\Ownership\OwnershipDetails\Monthly",
    "@Region@\Ownership\OwnershipMonthlySummary\Monthly",
    "@Region@\Ownership\OwnershipSummary\Monthly",
    "@Region@\Ownership\UKMajorShareholderTransactions\Monthly",
    "@Region@\Price\AlphaBeta\Monthly",
    "@Region@\Price\HistoricalReturns\Monthly",
    "@Region@\Price\Price\Monthly",
    "@Region@\Price\RawPrice\Monthly",
    "@Region@\Reference\CompanyReference\Monthly",
    "@Region@\Reference\SecurityReference\Monthly",
    "@Region@\Reference\Advisor\Monthly",
    "@Region@\ReturnAndPrice\AlphaBeta\Monthly",
    "@Region@\ReturnAndPrice\HistoricalReturns\Monthly",
    "@Region@\SEDOL\SEDOL\Monthly",
    "@Region@\ShortInterest\ShortInterest\Monthly"
]
region = ["AFR", "ANZ", "ASP", "EUR", "IPM", "LTA", "NRA", "UKI"]

for r in region:
    for f in folder:
        path = root + f.replace("@Region@", r)
        if not os.path.exists(path):
            print(path)
print("RegionTest1")

root2 = "D:\QA\GEDF\GeDataFeed-MOCAL4936\GEDF\Deadwood\\"
folder2 = [
    "@Region@\AssetClassification\AssetClassification\Monthly",
    "@Region@\AssetClassification\AssetClassificationHistory\Monthly",
    
    "@Region@\CompanyProfile\GeneralProfile\Monthly",
    "@Region@\CompanyProfile\IndexDJ\Monthly",
    "@Region@\CompanyProfile\IndexSNP\Monthly",
    "@Region@\CompanyProfile\LongDescription\Monthly",
    "@Region@\CompanyProfile\MediumDescription\Monthly",

    "@Region@\CorporateAction\CapitalRepayment\Monthly",
    "@Region@\CorporateAction\CashDividend\Monthly",
    "@Region@\CorporateAction\MergerAndAcquisition\Monthly",
    "@Region@\CorporateAction\RightsIssue\Monthly",
    "@Region@\CorporateAction\SpinOff\Monthly",
    "@Region@\CorporateAction\StockSplit\Monthly",

    "@Region@\CUSIPandISIN\CUSIPandISIN\Monthly",

    "@Region@\ExecutiveInsight\BoardCompensationCurrent\Monthly",
    "@Region@\ExecutiveInsight\BoardCompensationHistory\Monthly",
    "@Region@\ExecutiveInsight\ExecutiveCompensationCurrent\Monthly",
    "@Region@\ExecutiveInsight\ExecutiveCompensationHistory\Monthly",
    "@Region@\ExecutiveInsight\MembershipCurrent\Monthly",
    "@Region@\ExecutiveInsight\MembershipHistory\Monthly",
    "@Region@\ExecutiveInsight\OfficerDirectorCurrent\Monthly",
    "@Region@\ExecutiveInsight\OfficerDirectorHistory\Monthly",
    "@Region@\ExecutiveInsight\OptionsExeCurrent\Monthly",
    "@Region@\ExecutiveInsight\OptionsExeHistory\Monthly",
    "@Region@\ExecutiveInsight\OutstandingAwardsCurrent\Monthly",
    "@Region@\ExecutiveInsight\OutstandingAwardsHistory\Monthly",
    "@Region@\ExecutiveInsight\StockOptionGrantCurrent\Monthly",
    "@Region@\ExecutiveInsight\StockOptionGrantHistory\Monthly",

    "@Region@\Fundamental\EarningRatios\Monthly",
    "@Region@\Fundamental\EarningReports\Monthly",
    "@Region@\Fundamental\FinancialStatements\Monthly",
    "@Region@\Fundamental\OperationRatios\Monthly",
    "@Region@\Fundamental\PriceMultipleRatios\Monthly",
    "@Region@\Fundamental\Segmentation\Monthly",
    "@Region@\Fundamental\ValuationRatios\Monthly",

    "@Region@\GlobalCorporationAction\MergerAndAcquisition\Monthly",
    "@Region@\GlobalCorporationAction\ShareCorporateActions\Monthly",

    "@Region@\Ownership\OwnershipDetails\Monthly",
    "@Region@\Ownership\OwnershipMonthlySummary\Monthly",
    "@Region@\Ownership\OwnershipSummary\Monthly",

    "@Region@\Price\AlphaBeta\Monthly",
    "@Region@\Price\HistoricalReturns\Monthly",
    "@Region@\Price\Price\Monthly",
    "@Region@\Price\RawPrice\Monthly",

    "@Region@\Reference\CompanyReference\Monthly",
    "@Region@\Reference\SecurityReference\Monthly",

    # "@Region@\ReturnAndPrice\AlphaBeta\Monthly",
    # "@Region@\ReturnAndPrice\HistoricalReturns\Monthly",
    "@Region@\SEDOL\SEDOL\Monthly",

    "@Region@\ShortInterest\ShortInterest\Monthly"
]

for r in region:
    for f in folder2:
        path = root2 + f.replace("@Region@", r)
        if not os.path.exists(path):
            print(path)