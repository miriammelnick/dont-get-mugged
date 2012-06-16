
###############################################################################
#
# UKPostalCodes
# Verifies that a given zip code matches the format expected for UK addresses.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UKPostalCodes(Choreography):

    """
    Create a new instance of the UKPostalCodes Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Validation/UKPostalCodes')


    def new_input_set(self):
        return UKPostalCodesInputSet()

    def _make_result_set(self, result, path):
        return UKPostalCodesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UKPostalCodesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UKPostalCodes
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UKPostalCodesInputSet(InputSet):
        """
        Set the value of the ZipCode input for this choreography. ((required, string) The zip code to validate.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the UKPostalCodes choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UKPostalCodesResultSet(ResultSet):
        """
        Retrieve the value for the "Match" output from this choreography execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        def get_Match(self):
            return self._output.get('Match', None)

class UKPostalCodesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UKPostalCodesResultSet(response, path)
