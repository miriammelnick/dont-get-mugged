
###############################################################################
#
# RetrieveBug
# Retrieve detailed information for a specifed Bug ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveBug(Choreography):

    """
    Create a new instance of the RetrieveBug Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/RetrieveBug')


    def new_input_set(self):
        return RetrieveBugInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBugResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBugChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveBug
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveBugInputSet(InputSet):
        """
        Set the value of the BugID input for this choreography. ((required, integer) Enter a Bug ID, for which information will be retrieved.)
        """
        def set_BugID(self, value):
            InputSet._set_input(self, 'BugID', value)

        """
        Set the value of the IncludeFields input for this choreography. ((optional, string) Enter additional parameters to expand the scope of information returned.  For full bug fetch: _all; Or, a comma-separated list: _default, comments, history, attachments.data)
        """
        def set_IncludeFields(self, value):
            InputSet._set_input(self, 'IncludeFields', value)

        """
        Set the value of the Password input for this choreography. ((optional, string) Your Bugzilla password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Server input for this choreography. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Username input for this choreography. ((optional, string) Your Bugzilla username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveBug choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveBugResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Bugzilla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveBugChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveBugResultSet(response, path)
