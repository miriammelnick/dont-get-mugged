
###############################################################################
#
# LinkLookup
# Used to lookup a bitly link with a given long URL.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LinkLookup(Choreography):

    """
    Create a new instance of the LinkLookup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bitly/Links/LinkLookup')


    def new_input_set(self):
        return LinkLookupInputSet()

    def _make_result_set(self, result, path):
        return LinkLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LinkLookupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LinkLookup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LinkLookupInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The oAuth access token provided by Bitly.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the URL input for this choreography. ((required, string) One or more long URLs to lookup.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)


"""
A ResultSet with methods tailored to the values returned by the LinkLookup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LinkLookupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Bitly.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LinkLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LinkLookupResultSet(response, path)
