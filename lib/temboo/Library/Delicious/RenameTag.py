
###############################################################################
#
# RenameTag
# Renames a specified tag.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RenameTag(Choreography):

    """
    Create a new instance of the RenameTag Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/RenameTag')


    def new_input_set(self):
        return RenameTagInputSet()

    def _make_result_set(self, result, path):
        return RenameTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameTagChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RenameTag
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RenameTagInputSet(InputSet):
        """
        Set the value of the NewTag input for this choreography. ((string) The new tag name.)
        """
        def set_NewTag(self, value):
            InputSet._set_input(self, 'NewTag', value)

        """
        Set the value of the OldTag input for this choreography. ((string) The existing tag to rename.)
        """
        def set_OldTag(self, value):
            InputSet._set_input(self, 'OldTag', value)

        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the RenameTag choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RenameTagResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RenameTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RenameTagResultSet(response, path)
