
###############################################################################
#
# SearchForUsers
# Search for a specified Bugzilla user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchForUsers(Choreography):

    """
    Create a new instance of the SearchForUsers Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/SearchForUsers')


    def new_input_set(self):
        return SearchForUsersInputSet()

    def _make_result_set(self, result, path):
        return SearchForUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForUsersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchForUsers
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchForUsersInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Bugzilla password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SearchForUser input for this choreography. ((required, string) Enter the usename to be querried.)
        """
        def set_SearchForUser(self, value):
            InputSet._set_input(self, 'SearchForUser', value)

        """
        Set the value of the Server input for this choreography. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Bugzilla username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SearchForUsers choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchForUsersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Bugzilla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchForUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForUsersResultSet(response, path)
