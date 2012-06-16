
###############################################################################
#
# BestSellerListByDate
# Retrieves data from a New York Times best-seller list for a specified date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class BestSellerListByDate(Choreography):

    """
    Create a new instance of the BestSellerListByDate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/BestSellers/BestSellerListByDate')


    def new_input_set(self):
        return BestSellerListByDateInputSet()

    def _make_result_set(self, result, path):
        return BestSellerListByDateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BestSellerListByDateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the BestSellerListByDate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BestSellerListByDateInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The API Key provided by NY Times)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Date input for this choreography. ((date) The best-seller list publication date. Can be an epoch timestamp in milliseconds or in YYYY-MM-DD format.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the ListName input for this choreography. ((string) The Times best-seller list to retrieve (i.e. e-book-fiction or hardcover-fiction))
        """
        def set_ListName(self, value):
            InputSet._set_input(self, 'ListName', value)


"""
A ResultSet with methods tailored to the values returned by the BestSellerListByDate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BestSellerListByDateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from the NY Times API)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BestSellerListByDateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BestSellerListByDateResultSet(response, path)
