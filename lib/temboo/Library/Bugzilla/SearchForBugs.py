
###############################################################################
#
# SearchForBugs
# Search for bugs listed by Mozilla product name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchForBugs(Choreography):

    """
    Create a new instance of the SearchForBugs Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/SearchForBugs')


    def new_input_set(self):
        return SearchForBugsInputSet()

    def _make_result_set(self, result, path):
        return SearchForBugsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForBugsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchForBugs
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchForBugsInputSet(InputSet):
        """
        Set the value of the BugChangeDate input for this choreography. ((optional, string) Retrieve bugs that were changed within a certain date range. For example: 25d will return all bugs changed from 25 days ago untill today.  Or: 3h, to return all bugs entered with 3 hours.)
        """
        def set_BugChangeDate(self, value):
            InputSet._set_input(self, 'BugChangeDate', value)

        """
        Set the value of the Password input for this choreography. ((optional, string) Your Bugzilla password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Priority input for this choreography. ((optional, integer) Filter results by priority: For example: enter P1, to get Priority 1 bugs assoicated with a Product.)
        """
        def set_Priority(self, value):
            InputSet._set_input(self, 'Priority', value)

        """
        Set the value of the Product input for this choreography. ((required, string) Enter the Mozilla product for which bugs will be retrieved. For example: Bugzilla)
        """
        def set_Product(self, value):
            InputSet._set_input(self, 'Product', value)

        """
        Set the value of the Server input for this choreography. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        def set_Server(self, value):
            InputSet._set_input(self, 'Server', value)

        """
        Set the value of the Severity input for this choreography. ((optional, string) Filter results by severity. For example: blocker)
        """
        def set_Severity(self, value):
            InputSet._set_input(self, 'Severity', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Bugzilla username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SearchForBugs choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchForBugsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Bugzilla.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchForBugsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForBugsResultSet(response, path)
