
###############################################################################
#
# GetAllBookmarks
# Returns all links posted to a Delicious account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllBookmarks(Choreography):

    """
    Create a new instance of the GetAllBookmarks Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetAllBookmarks')


    def new_input_set(self):
        return GetAllBookmarksInputSet()

    def _make_result_set(self, result, path):
        return GetAllBookmarksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllBookmarksChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllBookmarks
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllBookmarksInputSet(InputSet):
        """
        Set the value of the Count input for this choreography. ((optional, integer) The number of bookmarks to return. Defaults to 15.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the FromDate input for this choreography. ((optional, date) Return only bookmarks posted on this date and later. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        def set_FromDate(self, value):
            InputSet._set_input(self, 'FromDate', value)

        """
        Set the value of the Meta input for this choreography. ((optional, string) Specify "1" to include a change-detection signature for each item returned. Defaults to "0", or no meta attributes retained.)
        """
        def set_Meta(self, value):
            InputSet._set_input(self, 'Meta', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Tag input for this choreography. ((optional, string) Return only bookmrks tagged with this keyword.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the ToDate input for this choreography. ((optional, date) Return only bookmarks posted on this date and earlier. Enter in YYYY-MM-DDThh:mm:ssZ format.)
        """
        def set_ToDate(self, value):
            InputSet._set_input(self, 'ToDate', value)

        """
        Set the value of the Username input for this choreography. ((required, string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetAllBookmarks choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllBookmarksResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAllBookmarksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllBookmarksResultSet(response, path)
