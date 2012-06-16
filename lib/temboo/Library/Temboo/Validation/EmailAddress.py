
###############################################################################
#
# EmailAddress
# Verifies that a given email address matches an expected standard pattern.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class EmailAddress(Choreography):

    """
    Create a new instance of the EmailAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Validation/EmailAddress')


    def new_input_set(self):
        return EmailAddressInputSet()

    def _make_result_set(self, result, path):
        return EmailAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EmailAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the EmailAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class EmailAddressInputSet(InputSet):
        """
        Set the value of the EmailAddress input for this choreography. ((required, string) The email address to validate.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)


"""
A ResultSet with methods tailored to the values returned by the EmailAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class EmailAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Match" output from this choreography execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        def get_Match(self):
            return self._output.get('Match', None)

class EmailAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EmailAddressResultSet(response, path)
