
###############################################################################
#
# ShortenURL
# Returns a shortened URL for a long URL that you provide.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ShortenURL(Choreography):

    """
    Create a new instance of the ShortenURL Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/Links/ShortenURL')


    def new_input_set(self):
        return ShortenURLInputSet()

    def _make_result_set(self, result, path):
        return ShortenURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShortenURLChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ShortenURL
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ShortenURLInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the LongURL input for this choreography. ((required, string) The long url that you want to shorten.)
        """
        def set_LongURL(self, value):
            InputSet._set_input(self, 'LongURL', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Defaults to simple "txt" format which will just return the shortened URL. "json" and "xml" are also supported.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ShortenURL choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ShortenURLResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ShortenURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShortenURLResultSet(response, path)
