
###############################################################################
#
# GeocodeByAddress
# Converts a human-readable address into geographic coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GeocodeByAddress(Choreography):

    """
    Create a new instance of the GeocodeByAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Geocoding/GeocodeByAddress')


    def new_input_set(self):
        return GeocodeByAddressInputSet()

    def _make_result_set(self, result, path):
        return GeocodeByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GeocodeByAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GeocodeByAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GeocodeByAddressInputSet(InputSet):
        """
        Set the value of the Address input for this choreography. ((string) The address that you want to geocode.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the Bounds input for this choreography. ((optional, string) The bounding box of the viewport within which to bias geocode results more prominently.)
        """
        def set_Bounds(self, value):
            InputSet._set_input(self, 'Bounds', value)

        """
        Set the value of the Language input for this choreography. ((optional, string) The language in which to return results. Defaults to 'en' (English).)
        """
        def set_Language(self, value):
            InputSet._set_input(self, 'Language', value)

        """
        Set the value of the Region input for this choreography. ((optional, string) The region code, specified as a ccTLD ("top-level domain") two-character value. Defaults to 'us' (United States).)
        """
        def set_Region(self, value):
            InputSet._set_input(self, 'Region', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the geocoding request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)


"""
A ResultSet with methods tailored to the values returned by the GeocodeByAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GeocodeByAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GeocodeByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GeocodeByAddressResultSet(response, path)
