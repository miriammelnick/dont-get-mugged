
###############################################################################
#
# CreateSharingPermission
# Grants a new user read/write access to an existing document.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateSharingPermission(Choreography):

    """
    Create a new instance of the CreateSharingPermission Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/CreateSharingPermission')


    def new_input_set(self):
        return CreateSharingPermissionInputSet()

    def _make_result_set(self, result, path):
        return CreateSharingPermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSharingPermissionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateSharingPermission
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateSharingPermissionInputSet(InputSet):
        """
        Set the value of the NewUserEmail input for this choreography. ((required, string) The email address of the user to whom you want to grant permission.)
        """
        def set_NewUserEmail(self, value):
            InputSet._set_input(self, 'NewUserEmail', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google passsword.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Role input for this choreography. ((optional, string) The role that will be given to the new user permission (i.e., writer, reader, etc). Defaults to "writer".)
        """
        def set_Role(self, value):
            InputSet._set_input(self, 'Role', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateSharingPermission choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateSharingPermissionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "ResourceID" output from this choreography execution. ((string) The resource ID of the document to which you want to add a user.)
        """
        def get_ResourceID(self):
            return self._output.get('ResourceID', None)

class CreateSharingPermissionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSharingPermissionResultSet(response, path)
