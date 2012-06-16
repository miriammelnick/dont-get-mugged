
###############################################################################
#
# SearchForShared
# Retrieves a list of all documents shared by the two users you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchForShared(Choreography):

    """
    Create a new instance of the SearchForShared Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchForShared')


    def new_input_set(self):
        return SearchForSharedInputSet()

    def _make_result_set(self, result, path):
        return SearchForSharedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForSharedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchForShared
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchForSharedInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the User1 input for this choreography. ((required, string) The email address of the first document collaborator.)
        """
        def set_User1(self, value):
            InputSet._set_input(self, 'User1', value)

        """
        Set the value of the User2 input for this choreography. ((required, string) The email address for the second document collaborator.)
        """
        def set_User2(self, value):
            InputSet._set_input(self, 'User2', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the SearchForShared choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchForSharedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchForSharedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForSharedResultSet(response, path)
