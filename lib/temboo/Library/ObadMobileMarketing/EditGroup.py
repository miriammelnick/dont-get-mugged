
###############################################################################
#
# EditGroup
# Allows you to create a new group or update an existing one.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EditGroup(Choreography):

    """
    Create a new instance of the EditGroup Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/EditGroup')


    def new_input_set(self):
        return EditGroupInputSet()

    def _make_result_set(self, result, path):
        return EditGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EditGroupChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EditGroup
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EditGroupInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ClientID input for this choreography. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Description input for this choreography. ((string) The description of the group)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the GroupID input for this choreography. ((integer) The id of the group you need to update. In creation mode, leave blank and the id will be returned in the response.)
        """
        def set_GroupID(self, value):
            InputSet._set_input(self, 'GroupID', value)

        """
        Set the value of the Mode input for this choreography. ((optional, boolean) Specify 0 for creating and 1 for updating. Defaults to 0.)
        """
        def set_Mode(self, value):
            InputSet._set_input(self, 'Mode', value)

        """
        Set the value of the Title input for this choreography. ((string) The title of the group)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of group to perform the action on.  Can be usergroup, shopgroup, or coupongroup. Defaults to usergroup.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the CSVData input for this choreography. ()
        """


"""
A ResultSet with methods tailored to the values returned by the EditGroup choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EditGroupResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class EditGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EditGroupResultSet(response, path)
