
###############################################################################
#
# GetAnalyticsByDate
# Retrieves anlaytics for your website for a particular date or date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAnalyticsByDate(Choreography):

    """
    Create a new instance of the GetAnalyticsByDate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Clicky/GetAnalyticsByDate')


    def new_input_set(self):
        return GetAnalyticsByDateInputSet()

    def _make_result_set(self, result, path):
        return GetAnalyticsByDateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAnalyticsByDateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAnalyticsByDate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAnalyticsByDateInputSet(InputSet):
        """
        Set the value of the Date input for this choreography. ((optional, string) The date or date range you want to access. Use YYYY-MM-DD format for date and YYYY-MM-DD,YYYY-MM-DD for a range. See docs for more options for this input. Defaults to 'today'.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The maximum number of results that will be returned. Defaults to 10.)
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
        Set the value of the Type input for this choreography. ((required, string) The type of data you want to retrieve. Can be a comma-separated list of types (i.e. visitors,countries,searches).)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the GetAnalyticsByDate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAnalyticsByDateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Clicky formatted as specified in the Output parameter. Default is XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAnalyticsByDateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAnalyticsByDateResultSet(response, path)
