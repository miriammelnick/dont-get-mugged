
###############################################################################
#
# GetBookmark
# Retrieves one or more bookmarked links posted on a single day.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBookmark(Choreography):

    """
    Create a new instance of the GetBookmark Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetBookmark')


    def new_input_set(self):
        return GetBookmarkInputSet()

    def _make_result_set(self, result, path):
        return GetBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBookmarkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBookmark
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBookmarkInputSet(InputSet):
        """
        Set the value of the ChangeSignature input for this choreography. ((optional, string) Return only bookmarks with the URL MD5 signatures you enter, regardless of posting date. Separate multiple signatures with spaces.)
        """
        def set_ChangeSignature(self, value):
            InputSet._set_input(self, 'ChangeSignature', value)

        """
        Set the value of the Date input for this choreography. ((optional, date) Return only bookmarks posted on a date specified here. Enter in YYYY-MM-DDThh:mm:ssZ format. Defaults to the most recent date.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

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
        Set the value of the Tag input for this choreography. ((optional, string) Return only items tagged with the specified keyword. Separate multiple tags with spaces.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the URL input for this choreography. ((optional, string) Return only items with the specified URL, regardless of posting date.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the Username input for this choreography. ((required, string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetBookmark choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBookmarkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBookmarkResultSet(response, path)
