
###############################################################################
#
# GetLocationElevation
# Obtain elevation information for a path generated by a set of geo-coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetLocationElevation(Choreography):

    """
    Create a new instance of the GetLocationElevation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Elevation/GetLocationElevation')


    def new_input_set(self):
        return GetLocationElevationInputSet()

    def _make_result_set(self, result, path):
        return GetLocationElevationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLocationElevationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetLocationElevation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetLocationElevationInputSet(InputSet):
        """
        Set the value of the Locations input for this choreography. ((required, string) Enter the location(s) for which elevation data will be obtained.  Input formats: a single latitude/longitude coordinate pair; an array of coordinates separated by a |. A set of encoded coordinates.)
        """
        def set_Locations(self, value):
            InputSet._set_input(self, 'Locations', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sensor input for this choreography. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        def set_Sensor(self, value):
            InputSet._set_input(self, 'Sensor', value)


"""
A ResultSet with methods tailored to the values returned by the GetLocationElevation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetLocationElevationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetLocationElevationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLocationElevationResultSet(response, path)
