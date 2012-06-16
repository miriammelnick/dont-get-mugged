
###############################################################################
#
# BestSellerHistory
# Retrieves data from a New York Times best-seller list for a specified title.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class BestSellerHistory(Choreography):

    """
    Create a new instance of the BestSellerHistory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/BestSellers/BestSellerHistory')


    def new_input_set(self):
        return BestSellerHistoryInputSet()

    def _make_result_set(self, result, path):
        return BestSellerHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BestSellerHistoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the BestSellerHistory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BestSellerHistoryInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The API Key provided by NY Times)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Title input for this choreography. ((string) The title of the best seller to retrieve data for)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)


"""
A ResultSet with methods tailored to the values returned by the BestSellerHistory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BestSellerHistoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from the NY Times API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BestSellerHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BestSellerHistoryResultSet(response, path)
