<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" labelsEnabled="1" maxScale="0" readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" version="3.12.3-București" simplifyMaxScale="1" simplifyLocal="1" styleCategories="AllStyleCategories" simplifyAlgorithm="0" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" type="RuleRenderer" symbollevels="0">
    <rules key="{a35e9511-cd02-4958-a73f-2e78890722de}">
      <rule symbol="0" filter=" &quot;floorspace&quot; /  area( $geometry) >= 0.2" label="Nykyinen rakennusten yhteenlaskettu kerrosala suhteessa ruudun pinta-alaan on vähintään 0,2" key="{c1426953-faac-415b-b74e-6368ed4539e1}"/>
      <rule symbol="1" filter="ELSE" label="muut ruudut" key="{fd14ec04-af59-45a4-b89d-06bb06885320}"/>
    </rules>
    <symbols>
      <symbol alpha="1" name="0" force_rhr="0" clip_to_extent="1" type="fill">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="222,65,120,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="1" force_rhr="0" clip_to_extent="1" type="fill">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="246,250,247,0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="dot"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fieldName="yhteensa_tco2" fontLetterSpacing="0" previewBkgrdColor="255,255,255,255" textOpacity="1" textColor="31,30,29,255" fontStrikeout="0" fontWordSpacing="0" fontUnderline="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOrientation="horizontal" fontFamily="MS Shell Dlg 2" namedStyle="Normaali" fontWeight="50" fontCapitals="0" fontSizeUnit="Point" blendMode="0" fontSize="5" isExpression="1" fontKerning="1" multilineHeight="1" fontItalic="0" useSubstitutions="0">
        <text-buffer bufferSize="1" bufferJoinStyle="128" bufferBlendMode="0" bufferDraw="0" bufferSizeUnits="MM" bufferColor="255,255,255,255" bufferOpacity="1" bufferNoFill="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <text-mask maskSize="0" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskSizeUnits="MM" maskOpacity="1" maskEnabled="0" maskJoinStyle="128" maskType="0" maskedSymbolLayers=""/>
        <background shapeRadiiUnit="MM" shapeOffsetUnit="MM" shapeDraw="0" shapeBorderWidth="0" shapeRotation="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiY="0" shapeType="0" shapeOffsetY="0" shapeFillColor="255,255,255,255" shapeBlendMode="0" shapeSVGFile="" shapeSizeX="0" shapeSizeType="0" shapeSizeY="0" shapeOffsetX="0" shapeRotationType="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeJoinStyle="64" shapeRadiiX="0" shapeOpacity="1" shapeSizeUnit="MM" shapeBorderWidthUnit="MM">
          <symbol alpha="1" name="markerSymbol" force_rhr="0" clip_to_extent="1" type="marker">
            <layer class="SimpleMarker" enabled="1" pass="0" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="125,139,143,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowBlendMode="6" shadowOpacity="0" shadowScale="100" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowRadius="0" shadowOffsetDist="1" shadowColor="0,0,0,255" shadowDraw="0" shadowOffsetAngle="135" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format addDirectionSymbol="0" autoWrapLength="3" formatNumbers="1" useMaxLineLengthForAutoWrap="1" decimals="1" plussign="0" rightDirectionSymbol=">" leftDirectionSymbol="&lt;" reverseDirectionSymbol="0" placeDirectionSymbol="0" wrapChar="" multilineAlign="0"/>
      <placement maxCurvedCharAngleOut="-25" offsetUnits="MapUnit" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="1" dist="0" maxCurvedCharAngleIn="25" offsetType="0" quadOffset="4" priority="10" repeatDistanceUnits="MM" placementFlags="10" geometryGenerator="" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" placement="1" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="90" rotationAngle="0" preserveRotation="1" centroidInside="1" geometryGeneratorEnabled="0" xOffset="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PolygonGeometry" repeatDistance="0" geometryGeneratorType="PointGeometry" overrunDistanceUnit="MM" overrunDistance="0" fitInPolygonOnly="0" distUnits="MM"/>
      <rendering obstacleFactor="1" labelPerPart="0" scaleMin="1000" obstacle="1" fontLimitPixelSize="0" maxNumLabels="2000" minFeatureSize="0" displayAll="1" scaleMax="25000" drawLabels="1" obstacleType="0" mergeLines="0" scaleVisibility="1" fontMaxPixelSize="10000" limitNumLabels="0" fontMinPixelSize="3" upsidedownLabels="0" zIndex="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="0" name="enabled" type="QString"/>
          <Option value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot;>&lt;layer class=&quot;SimpleLine&quot; enabled=&quot;1&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>fid</value>
    </property>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <LinearlyInterpolatedDiagramRenderer classificationAttributeExpression=" &quot;vesi_tco2&quot; + &quot;lammitys_tco2&quot; + &quot;jaahdytys_tco2&quot; + &quot;kiinteistosahko_tco2&quot; + &quot;sahko_kotitaloudet_tco2&quot; + &quot;sahko_palv_tco2&quot; + &quot;sahko_tv_tco2&quot; + &quot;hloliikenne_ap_tco2&quot; + &quot;hloliikenne_tp_tco2&quot; + &quot;tvliikenne_tco2&quot; + &quot;palvliikenne_tco2&quot; + &quot;korjaussaneeraus_tco2&quot; " attributeLegend="1" upperWidth="10" upperValue="12138.6" lowerWidth="0" upperHeight="10" lowerHeight="0" lowerValue="0" diagramType="Pie">
    <DiagramCategory spacingUnit="MM" penColor="#ffffff" backgroundAlpha="255" rotationOffset="270" showAxis="0" lineSizeType="MM" minimumSize="3" width="15" spacingUnitScale="3x:0,0,0,0,0,0" scaleBasedVisibility="1" backgroundColor="#ffffff" sizeScale="3x:0,0,0,0,0,0" barWidth="5" spacing="0" scaleDependency="Area" penAlpha="255" lineSizeScale="3x:0,0,0,0,0,0" opacity="1" sizeType="MM" height="15" enabled="0" penWidth="0.1" direction="1" maxScaleDenominator="50000" minScaleDenominator="1000" labelPlacementMethod="XHeight" diagramOrientation="Up">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="lammitys_tco2" color="#ca4d41" label="Lämmitys"/>
      <attribute field="vesi_tco2" color="#418aca" label="Vesi"/>
      <attribute field="hloliikenne_ap_tco2" color="#c551bc" label="Henkilöliikenne, ap"/>
      <attribute field="sahko_kotitaloudet_tco2" color="#ecff3b" label="Sähkö, kotitaloudet"/>
      <attribute field="palvliikenne_tco2" color="#745d7c" label="Palveluliikenne"/>
      <attribute field="sahko_palv_tco2" color="#decd98" label="Sähkö, palvelut"/>
      <attribute field="tvliikenne_tco2" color="#661f98" label="Liikenne, tv"/>
      <attribute field="sahko_tv_tco2" color="#bbf7d6" label="Sähkö, tv"/>
      <attribute field="kiinteistosahko_tco2" color="#3a2f6c" label="Kiinteistösähkö"/>
      <attribute field="hloliikenne_tp_tco2" color="#4dee3b" label="Henkilöliikenne, tp"/>
      <attribute field="korjaussaneeraus_tco2" color="#d6a4ff" label="Korjaussaneeraus"/>
      <attribute field="jaahdytys_tco2" color="#51c7bc" label="Jäähdytys"/>
      <axisSymbol>
        <symbol alpha="1" name="" force_rhr="0" clip_to_extent="1" type="line">
          <layer class="SimpleLine" enabled="1" pass="0" locked="0">
            <prop k="capstyle" v="square"/>
            <prop k="customdash" v="5;2"/>
            <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="customdash_unit" v="MM"/>
            <prop k="draw_inside_polygon" v="0"/>
            <prop k="joinstyle" v="bevel"/>
            <prop k="line_color" v="35,35,35,255"/>
            <prop k="line_style" v="solid"/>
            <prop k="line_width" v="0.26"/>
            <prop k="line_width_unit" v="MM"/>
            <prop k="offset" v="0"/>
            <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <prop k="offset_unit" v="MM"/>
            <prop k="ring_filter" v="0"/>
            <prop k="use_custom_dash" v="0"/>
            <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </LinearlyInterpolatedDiagramRenderer>
  <DiagramLayerSettings placement="4" linePlacementFlags="18" dist="0" obstacle="0" zIndex="0" showAll="1" priority="10">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option value="0" name="allowedGapsBuffer" type="double"/>
        <Option value="false" name="allowedGapsEnabled" type="bool"/>
        <Option value="" name="allowedGapsLayer" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="xyind">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="mun">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="zone">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="year">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="floorspace">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pop">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tilat_vesi_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tilat_lammitys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tilat_jaahdytys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_kiinteistot_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_kotitaloudet_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_hlo_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rak_korjaussaneeraus_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rak_purku_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="rak_uudis_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_lammonsaato_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_liikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_sahko_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_rakentaminen_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tp_yht">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pop_per_popjob_percentage">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2_per_asukas">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2_per_tp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2_per_as_tp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sum_yhteensa_tco2_per_kem">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="xyind" index="0" name=""/>
    <alias field="mun" index="1" name=""/>
    <alias field="zone" index="2" name=""/>
    <alias field="year" index="3" name=""/>
    <alias field="floorspace" index="4" name=""/>
    <alias field="pop" index="5" name=""/>
    <alias field="tilat_vesi_tco2" index="6" name=""/>
    <alias field="tilat_lammitys_tco2" index="7" name=""/>
    <alias field="tilat_jaahdytys_tco2" index="8" name=""/>
    <alias field="sahko_kiinteistot_tco2" index="9" name=""/>
    <alias field="sahko_kotitaloudet_tco2" index="10" name=""/>
    <alias field="sahko_palv_tco2" index="11" name=""/>
    <alias field="sahko_tv_tco2" index="12" name=""/>
    <alias field="liikenne_hlo_tco2" index="13" name=""/>
    <alias field="liikenne_tv_tco2" index="14" name=""/>
    <alias field="liikenne_palv_tco2" index="15" name=""/>
    <alias field="rak_korjaussaneeraus_tco2" index="16" name=""/>
    <alias field="rak_purku_tco2" index="17" name=""/>
    <alias field="rak_uudis_tco2" index="18" name=""/>
    <alias field="sum_yhteensa_tco2" index="19" name=""/>
    <alias field="sum_lammonsaato_tco2" index="20" name=""/>
    <alias field="sum_liikenne_tco2" index="21" name=""/>
    <alias field="sum_sahko_tco2" index="22" name=""/>
    <alias field="sum_rakentaminen_tco2" index="23" name=""/>
    <alias field="tp_yht" index="24" name=""/>
    <alias field="pop_per_popjob_percentage" index="25" name=""/>
    <alias field="sum_yhteensa_tco2_per_asukas" index="26" name=""/>
    <alias field="sum_yhteensa_tco2_per_tp" index="27" name=""/>
    <alias field="sum_yhteensa_tco2_per_as_tp" index="28" name=""/>
    <alias field="sum_yhteensa_tco2_per_kem" index="29" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="xyind" applyOnUpdate="0" expression=""/>
    <default field="mun" applyOnUpdate="0" expression=""/>
    <default field="zone" applyOnUpdate="0" expression=""/>
    <default field="year" applyOnUpdate="0" expression=""/>
    <default field="floorspace" applyOnUpdate="0" expression=""/>
    <default field="pop" applyOnUpdate="0" expression=""/>
    <default field="tilat_vesi_tco2" applyOnUpdate="0" expression=""/>
    <default field="tilat_lammitys_tco2" applyOnUpdate="0" expression=""/>
    <default field="tilat_jaahdytys_tco2" applyOnUpdate="0" expression=""/>
    <default field="sahko_kiinteistot_tco2" applyOnUpdate="0" expression=""/>
    <default field="sahko_kotitaloudet_tco2" applyOnUpdate="0" expression=""/>
    <default field="sahko_palv_tco2" applyOnUpdate="0" expression=""/>
    <default field="sahko_tv_tco2" applyOnUpdate="0" expression=""/>
    <default field="liikenne_hlo_tco2" applyOnUpdate="0" expression=""/>
    <default field="liikenne_tv_tco2" applyOnUpdate="0" expression=""/>
    <default field="liikenne_palv_tco2" applyOnUpdate="0" expression=""/>
    <default field="rak_korjaussaneeraus_tco2" applyOnUpdate="0" expression=""/>
    <default field="rak_purku_tco2" applyOnUpdate="0" expression=""/>
    <default field="rak_uudis_tco2" applyOnUpdate="0" expression=""/>
    <default field="sum_yhteensa_tco2" applyOnUpdate="0" expression=""/>
    <default field="sum_lammonsaato_tco2" applyOnUpdate="0" expression=""/>
    <default field="sum_liikenne_tco2" applyOnUpdate="0" expression=""/>
    <default field="sum_sahko_tco2" applyOnUpdate="0" expression=""/>
    <default field="sum_rakentaminen_tco2" applyOnUpdate="0" expression=""/>
    <default field="tp_yht" applyOnUpdate="0" expression=""/>
    <default field="pop_per_popjob_percentage" applyOnUpdate="0" expression=""/>
    <default field="sum_yhteensa_tco2_per_asukas" applyOnUpdate="0" expression=""/>
    <default field="sum_yhteensa_tco2_per_tp" applyOnUpdate="0" expression=""/>
    <default field="sum_yhteensa_tco2_per_as_tp" applyOnUpdate="0" expression=""/>
    <default field="sum_yhteensa_tco2_per_kem" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint notnull_strength="0" field="xyind" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="mun" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="zone" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="year" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="floorspace" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="pop" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="tilat_vesi_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="tilat_lammitys_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="tilat_jaahdytys_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sahko_kiinteistot_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sahko_kotitaloudet_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sahko_palv_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sahko_tv_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="liikenne_hlo_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="liikenne_tv_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="liikenne_palv_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="rak_korjaussaneeraus_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="rak_purku_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="rak_uudis_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_yhteensa_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_lammonsaato_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_liikenne_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_sahko_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_rakentaminen_tco2" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="tp_yht" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="pop_per_popjob_percentage" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_yhteensa_tco2_per_asukas" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_yhteensa_tco2_per_tp" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_yhteensa_tco2_per_as_tp" constraints="0" exp_strength="0" unique_strength="0"/>
    <constraint notnull_strength="0" field="sum_yhteensa_tco2_per_kem" constraints="0" exp_strength="0" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="xyind" desc=""/>
    <constraint exp="" field="mun" desc=""/>
    <constraint exp="" field="zone" desc=""/>
    <constraint exp="" field="year" desc=""/>
    <constraint exp="" field="floorspace" desc=""/>
    <constraint exp="" field="pop" desc=""/>
    <constraint exp="" field="tilat_vesi_tco2" desc=""/>
    <constraint exp="" field="tilat_lammitys_tco2" desc=""/>
    <constraint exp="" field="tilat_jaahdytys_tco2" desc=""/>
    <constraint exp="" field="sahko_kiinteistot_tco2" desc=""/>
    <constraint exp="" field="sahko_kotitaloudet_tco2" desc=""/>
    <constraint exp="" field="sahko_palv_tco2" desc=""/>
    <constraint exp="" field="sahko_tv_tco2" desc=""/>
    <constraint exp="" field="liikenne_hlo_tco2" desc=""/>
    <constraint exp="" field="liikenne_tv_tco2" desc=""/>
    <constraint exp="" field="liikenne_palv_tco2" desc=""/>
    <constraint exp="" field="rak_korjaussaneeraus_tco2" desc=""/>
    <constraint exp="" field="rak_purku_tco2" desc=""/>
    <constraint exp="" field="rak_uudis_tco2" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2" desc=""/>
    <constraint exp="" field="sum_lammonsaato_tco2" desc=""/>
    <constraint exp="" field="sum_liikenne_tco2" desc=""/>
    <constraint exp="" field="sum_sahko_tco2" desc=""/>
    <constraint exp="" field="sum_rakentaminen_tco2" desc=""/>
    <constraint exp="" field="tp_yht" desc=""/>
    <constraint exp="" field="pop_per_popjob_percentage" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2_per_asukas" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2_per_tp" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2_per_as_tp" desc=""/>
    <constraint exp="" field="sum_yhteensa_tco2_per_kem" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" name="xyind" type="field" hidden="0"/>
      <column width="202" name="sahko_kotitaloudet_tco2" type="field" hidden="0"/>
      <column width="-1" name="sahko_palv_tco2" type="field" hidden="0"/>
      <column width="-1" name="sahko_tv_tco2" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
      <column width="-1" name="tilat_vesi_tco2" type="field" hidden="0"/>
      <column width="-1" name="tilat_lammitys_tco2" type="field" hidden="0"/>
      <column width="-1" name="tilat_jaahdytys_tco2" type="field" hidden="0"/>
      <column width="-1" name="sahko_kiinteistot_tco2" type="field" hidden="0"/>
      <column width="-1" name="liikenne_hlo_tco2" type="field" hidden="0"/>
      <column width="-1" name="liikenne_tv_tco2" type="field" hidden="0"/>
      <column width="-1" name="liikenne_palv_tco2" type="field" hidden="0"/>
      <column width="-1" name="rak_korjaussaneeraus_tco2" type="field" hidden="0"/>
      <column width="-1" name="rak_purku_tco2" type="field" hidden="0"/>
      <column width="-1" name="rak_uudis_tco2" type="field" hidden="0"/>
      <column width="-1" name="sum_yhteensa_tco2" type="field" hidden="0"/>
      <column width="-1" name="sum_lammonsaato_tco2" type="field" hidden="0"/>
      <column width="-1" name="sum_liikenne_tco2" type="field" hidden="0"/>
      <column width="-1" name="sum_sahko_tco2" type="field" hidden="0"/>
      <column width="-1" name="sum_rakentaminen_tco2" type="field" hidden="0"/>
      <column width="-1" name="mun" type="field" hidden="0"/>
      <column width="-1" name="zone" type="field" hidden="0"/>
      <column width="-1" name="year" type="field" hidden="0"/>
      <column width="-1" name="floorspace" type="field" hidden="0"/>
      <column width="-1" name="pop" type="field" hidden="0"/>
      <column width="-1" name="sum_yhteensa_tco2_per_asukas" type="field" hidden="0"/>
      <column width="-1" name="tp_yht" type="field" hidden="0"/>
      <column width="-1" name="sum_yhteensa_tco2_per_tp" type="field" hidden="0"/>
      <column width="-1" name="sum_yhteensa_tco2_per_as_tp" type="field" hidden="0"/>
      <column width="-1" name="sum_yhteensa_tco2_per_kem" type="field" hidden="0"/>
      <column width="-1" name="pop_per_popjob_percentage" type="field" hidden="0"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.
Use this function to add extra logic to your forms.
Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="fid" editable="1"/>
    <field name="floorspace" editable="1"/>
    <field name="hloliikenne_ap_tco2" editable="1"/>
    <field name="hloliikenne_tco2" editable="1"/>
    <field name="hloliikenne_tp_tco2" editable="1"/>
    <field name="id" editable="1"/>
    <field name="jaahdytys_tco2" editable="1"/>
    <field name="kiinteistosahko_tco2" editable="1"/>
    <field name="korjaussaneeraus_tco2" editable="1"/>
    <field name="lammitys_tco2" editable="1"/>
    <field name="liikenne_hlo_tco2" editable="1"/>
    <field name="liikenne_palv_tco2" editable="1"/>
    <field name="liikenne_tv_tco2" editable="1"/>
    <field name="liikenne_yht" editable="1"/>
    <field name="mun" editable="1"/>
    <field name="palvliikenne_tco2" editable="1"/>
    <field name="pop" editable="1"/>
    <field name="pop_per_popjob_percentage" editable="1"/>
    <field name="purkaminen_tco2" editable="1"/>
    <field name="rak_korjaussaneeraus_tco2" editable="1"/>
    <field name="rak_purku_tco2" editable="1"/>
    <field name="rak_uudis_tco2" editable="1"/>
    <field name="sahko_kiinteistot_tco2" editable="1"/>
    <field name="sahko_kotitaloudet_tco2" editable="1"/>
    <field name="sahko_palv_tco2" editable="1"/>
    <field name="sahko_tv_tco2" editable="1"/>
    <field name="sahko_yht" editable="1"/>
    <field name="sum_lammonsaato_tco2" editable="1"/>
    <field name="sum_liikenne_tco2" editable="1"/>
    <field name="sum_rakentaminen_tco2" editable="1"/>
    <field name="sum_sahko_tco2" editable="1"/>
    <field name="sum_yhteensa_tco2" editable="1"/>
    <field name="sum_yhteensa_tco2_per_as_tp" editable="1"/>
    <field name="sum_yhteensa_tco2_per_asukas" editable="1"/>
    <field name="sum_yhteensa_tco2_per_kem" editable="1"/>
    <field name="sum_yhteensa_tco2_per_tp" editable="1"/>
    <field name="summa" editable="1"/>
    <field name="tilat_jaahdytys_tco2" editable="1"/>
    <field name="tilat_lammitys_tco2" editable="1"/>
    <field name="tilat_vesi_tco2" editable="1"/>
    <field name="tp_yht" editable="1"/>
    <field name="tvliikenne_tco2" editable="1"/>
    <field name="uudisrakentaminen_tco2" editable="1"/>
    <field name="vesi_tco2" editable="1"/>
    <field name="vuosi" editable="1"/>
    <field name="xyind" editable="1"/>
    <field name="year" editable="1"/>
    <field name="yhteensa_tco2" editable="1"/>
    <field name="zone" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="fid" labelOnTop="0"/>
    <field name="floorspace" labelOnTop="0"/>
    <field name="hloliikenne_ap_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tp_tco2" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="jaahdytys_tco2" labelOnTop="0"/>
    <field name="kiinteistosahko_tco2" labelOnTop="0"/>
    <field name="korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="lammitys_tco2" labelOnTop="0"/>
    <field name="liikenne_hlo_tco2" labelOnTop="0"/>
    <field name="liikenne_palv_tco2" labelOnTop="0"/>
    <field name="liikenne_tv_tco2" labelOnTop="0"/>
    <field name="liikenne_yht" labelOnTop="0"/>
    <field name="mun" labelOnTop="0"/>
    <field name="palvliikenne_tco2" labelOnTop="0"/>
    <field name="pop" labelOnTop="0"/>
    <field name="pop_per_popjob_percentage" labelOnTop="0"/>
    <field name="purkaminen_tco2" labelOnTop="0"/>
    <field name="rak_korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="rak_purku_tco2" labelOnTop="0"/>
    <field name="rak_uudis_tco2" labelOnTop="0"/>
    <field name="sahko_kiinteistot_tco2" labelOnTop="0"/>
    <field name="sahko_kotitaloudet_tco2" labelOnTop="0"/>
    <field name="sahko_palv_tco2" labelOnTop="0"/>
    <field name="sahko_tv_tco2" labelOnTop="0"/>
    <field name="sahko_yht" labelOnTop="0"/>
    <field name="sum_lammonsaato_tco2" labelOnTop="0"/>
    <field name="sum_liikenne_tco2" labelOnTop="0"/>
    <field name="sum_rakentaminen_tco2" labelOnTop="0"/>
    <field name="sum_sahko_tco2" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_as_tp" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_asukas" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_kem" labelOnTop="0"/>
    <field name="sum_yhteensa_tco2_per_tp" labelOnTop="0"/>
    <field name="summa" labelOnTop="0"/>
    <field name="tilat_jaahdytys_tco2" labelOnTop="0"/>
    <field name="tilat_lammitys_tco2" labelOnTop="0"/>
    <field name="tilat_vesi_tco2" labelOnTop="0"/>
    <field name="tp_yht" labelOnTop="0"/>
    <field name="tvliikenne_tco2" labelOnTop="0"/>
    <field name="uudisrakentaminen_tco2" labelOnTop="0"/>
    <field name="vesi_tco2" labelOnTop="0"/>
    <field name="vuosi" labelOnTop="0"/>
    <field name="xyind" labelOnTop="0"/>
    <field name="year" labelOnTop="0"/>
    <field name="yhteensa_tco2" labelOnTop="0"/>
    <field name="zone" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
