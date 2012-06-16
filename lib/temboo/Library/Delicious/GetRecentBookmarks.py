
###############################################################################
#
# GetRecentBookmarks
# Retrieve a list of the most recently posted bookmarks.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecentBookmarks(Choreography):

    """
    Create a new instance of the GetRecentBookmarks Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetRecentBookmarks')


    def new_input_set(self):
        return GetRecentBookmarksInputSet()

    def _make_result_set(self, result, path):
        return GetRecentBookmarksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentBookmarksChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecentBookmarks
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecentBookmarksInputSet(InputSet):
        """
        Set the value of the Count input for this choreography. ((optional, integer) Specify the number of bookmarks to retrieve, up the maximum of 100. The default is 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) Return only items tagged with the specified keyword.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecentBookmarks choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecentBookmarksResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecentBookmarksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentBookmarksResultSet(response, path)
