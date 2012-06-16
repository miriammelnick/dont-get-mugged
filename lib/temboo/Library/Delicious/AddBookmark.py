
###############################################################################
#
# AddBookmark
# Adds a link bookmark to a Delicious account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddBookmark(Choreography):

    """
    Create a new instance of the AddBookmark Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/AddBookmark')


    def new_input_set(self):
        return AddBookmarkInputSet()

    def _make_result_set(self, result, path):
        return AddBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddBookmarkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddBookmark
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddBookmarkInputSet(InputSet):
        """
        Set the value of the Description input for this choreography. ((string) A description for the link to post.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Notes input for this choreography. ((optional, string) Descriptive notes for the posted link.)
        """
        def set_Notes(self, value):
            InputSet._set_input(self, 'Notes', value)

        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Replace input for this choreography. ((optional, integer) Specify "1" to replace the post if the URL has already been posted. Set to "0" (don't replace) by default.)
        """
        def set_Replace(self, value):
            InputSet._set_input(self, 'Replace', value)

        """
        Set the value of the Shared input for this choreography. ((optional, integer) Specify "1" to make the posted link private. Set to "0" (shared) by default.)
        """
        def set_Shared(self, value):
            InputSet._set_input(self, 'Shared', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) Add keyword tags to the posted link. Separate multiple tags with commas.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the URL input for this choreography. ((string) The URL for the link to post.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the AddBookmark choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddBookmarkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "Date" output from this choreography execution. ()
        """
        def get_Date(self):
            return self._output.get('Date', None)

class AddBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddBookmarkResultSet(response, path)
