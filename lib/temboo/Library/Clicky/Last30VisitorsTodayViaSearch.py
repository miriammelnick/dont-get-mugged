
###############################################################################
#
# Last30VisitorsTodayViaSearch
# Retrieves the last 30 visitors today who arrived via a search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Last30VisitorsTodayViaSearch(Choreography):

    """
    Create a new instance of the Last30VisitorsTodayViaSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Clicky/Last30VisitorsTodayViaSearch')


    def new_input_set(self):
        return Last30VisitorsTodayViaSearchInputSet()

    def _make_result_set(self, result, path):
        return Last30VisitorsTodayViaSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return Last30VisitorsTodayViaSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Last30VisitorsTodayViaSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class Last30VisitorsTodayViaSearchInputSet(InputSet):
        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of records you want to retrieve. Defaults to 30.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Output input for this choreography. ((optional, string) What format you want the returned data to be in. Accepted values: xml, php, json, csv. Defaults to 'xml'.)
        """
        def set_Output(self, value):
            InputSet._set_input(self, 'Output', value)

        """
        Set the value of the SiteID input for this choreography. ((required, integer) Your request must include the site's ID that you want to access data from. Available from your site preferences page.)
        """
        def set_SiteID(self, value):
            InputSet._set_input(self, 'SiteID', value)

        """
        Set the value of the SiteKey input for this choreography. ((required, string) The unique key assigned to you when you first register with Clicky. Available from your site preferences page.)
        """
        def set_SiteKey(self, value):
            InputSet._set_input(self, 'SiteKey', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of data you want to retrieve. Defaults to "visitors-list".)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the Last30VisitorsTodayViaSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class Last30VisitorsTodayViaSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class Last30VisitorsTodayViaSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return Last30VisitorsTodayViaSearchResultSet(response, path)
