
###############################################################################
#
# GetEncodersCount
# Returns the count of users who have shortened a specified bitly link.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetEncodersCount(Choreography):

    """
    Create a new instance of the GetEncodersCount Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/LinkMetrics/GetEncodersCount')


    def new_input_set(self):
        return GetEncodersCountInputSet()

    def _make_result_set(self, result, path):
        return GetEncodersCountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEncodersCountChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetEncodersCount
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetEncodersCountInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Link input for this choreography. ((required, string) A bitly link.)
        """
        def set_Link(self, value):
            InputSet._set_input(self, 'Link', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the GetEncodersCount choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetEncodersCountResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetEncodersCountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEncodersCountResultSet(response, path)
