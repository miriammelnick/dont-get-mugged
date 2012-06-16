
###############################################################################
#
# AccountFeedRequest
# Retrieves a list of Analytics profiles available to an authorized account user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AccountFeedRequest(Choreography):

    """
    Create a new instance of the AccountFeedRequest Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Analytics/AccountFeedRequest')


    def new_input_set(self):
        return AccountFeedRequestInputSet()

    def _make_result_set(self, result, path):
        return AccountFeedRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountFeedRequestChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AccountFeedRequest
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AccountFeedRequestInputSet(InputSet):
        """
        Set the value of the MaxResults input for this choreography. ((optional, integer) The max results to be returned in the feed. Defaults to 50.)
        """
        def set_MaxResults(self, value):
            InputSet._set_input(self, 'MaxResults', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the StartIndex input for this choreography. ((optional, integer) The starting entry for the feed. Defaults to 1.)
        """
        def set_StartIndex(self, value):
            InputSet._set_input(self, 'StartIndex', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account email address.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the AccountFeedRequest choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AccountFeedRequestResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AccountFeedRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountFeedRequestResultSet(response, path)
