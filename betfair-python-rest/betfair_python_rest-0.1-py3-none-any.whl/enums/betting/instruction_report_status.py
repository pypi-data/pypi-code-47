from ..base import BaseEnum


class ExecutionReportStatus(BaseEnum):
    SUCCESS = 'The instruction was successful.'

    FAILURE = 'The instruction failed.'

    TIMEOUT = '''The order timed out & the status of
     the bet is unknown.  If a TIMEOUT error 
     occurs on a placeOrders/replaceOrders 
     request, you should check listCurrentOrders 
     to verify the status of your bets before 
     placing further orders. Please Note: Timeouts 
     will occur after 5 seconds of attempting to process
      the bet but please allow up to 15 seconds for
       a timed out order to appear. After this 
       time any unprocessed bets will automatically
        be Lapsed and no longer be available on
         the Exchange.'''
