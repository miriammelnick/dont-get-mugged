
###############################################################################
#
# ListCoordinatesForZipcode
# Retrieve latitude and longitude data for a specified zipcode (in 50 U.S. States and Puerto Rico).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListCoordinatesForZipcode(Choreography):

    """
    Create a new instance of the ListCoordinatesForZipcode Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NOAA/ListCoordinatesForZipcode')


    def new_input_set(self):
        return ListCoordinatesForZipcodeInputSet()

    def _make_result_set(self, result, path):
        return ListCoordinatesForZipcodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCoordinatesForZipcodeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListCoordinatesForZipcode
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListCoordinatesForZipcodeInputSet(InputSet):
        """
        Set the value of the ListZipCodeList input for this choreography. ((integer) Enter the zipcode for which latitude and longitude coordinates will be retrieved.)
        """
        def set_ListZipCodeList(self, value):
            InputSet._set_input(self, 'ListZipCodeList', value)


"""
A ResultSet with methods tailored to the values returned by the ListCoordinatesForZipcode choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListCoordinatesForZipcodeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) Response from NDFD servers.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListCoordinatesForZipcodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCoordinatesForZipcodeResultSet(response, path)
